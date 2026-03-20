from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Course, Lesson, Enrollment, LessonProgress

def course_list(request):
    courses = Course.objects.filter(is_published=True).order_by('is_free', 'price')
    return render(request, 'lms/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk, is_published=True)
    lessons = course.lessons.all()
    enrollment = None
    progress_ids = []
    if request.user.is_authenticated:
        enrollment = Enrollment.objects.filter(user=request.user, course=course).first()
        if enrollment:
            progress_ids = list(enrollment.progress.values_list('lesson_id', flat=True))
    return render(request, 'lms/course_detail.html', {
        'course': course, 'lessons': lessons,
        'enrollment': enrollment, 'progress_ids': progress_ids
    })

@login_required
def enroll(request, pk):
    course = get_object_or_404(Course, pk=pk, is_published=True)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created:
        messages.success(request, f'Enrolled in "{course.title}"!')
    return redirect('course_detail', pk=pk)

@login_required
def lesson_view(request, course_pk, lesson_pk):
    course = get_object_or_404(Course, pk=course_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course=course)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)

    if request.method == 'POST' and 'mark_complete' in request.POST:
        LessonProgress.objects.get_or_create(enrollment=enrollment, lesson=lesson)
        total = course.lessons.count()
        done = enrollment.progress.count()
        if done >= total:
            enrollment.completed = True
            enrollment.completed_at = timezone.now()
            enrollment.save()
            messages.success(request, '🎉 Course completed! Certificate earned.')
        return redirect('lesson_view', course_pk=course_pk, lesson_pk=lesson_pk)

    progress_ids = list(enrollment.progress.values_list('lesson_id', flat=True))
    next_lesson = course.lessons.filter(order__gt=lesson.order).first()
    prev_lesson = course.lessons.filter(order__lt=lesson.order).last()
    return render(request, 'lms/lesson.html', {
        'course': course, 'lesson': lesson, 'enrollment': enrollment,
        'progress_ids': progress_ids, 'next_lesson': next_lesson, 'prev_lesson': prev_lesson,
        'is_complete': lesson.pk in progress_ids,
    })

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course').order_by('-enrolled_at')
    return render(request, 'lms/my_courses.html', {'enrollments': enrollments})
