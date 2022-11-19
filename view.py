from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Tasks


@api_view(['POST','GET','DELETE'])
def tasks_information(request,id_in_url):
    if request.method == 'POST':
        input_category=request.data.get("category")
        if input_category == "" or input_category == None:
            return Response(status=400)
        tasks=Tasks.objects.filter(task_id=id_in_url)
        if len(tasks)>=1:
            return Response(status=400)
        else:
            Tasks(task_id=id_in_url,category=input_category,status="pending").save()
            return Response(status=200)
    if request.method == 'DELETE':
        tasks=Tasks.objects.filter(task_id=id_in_url)
        if len(tasks)==0:
            return Response(status=404)
        else:
            Tasks.objects.filter(task_id=id_in_url).delete()
            return Response(status=200)
@api_view(['GET'])
def list_of_tasks(request):
    tasks=Tasks.objects.all()
    listofalltasks=[]
    for task in tasks:
        listofalltasks.append({
            "task_id":task.task_id,
            "category":task.category,
            "status":task.status
        })
    return Response(data={
        "list_of_Tasks":listofalltasks
    },status=200)
@api_view(['GET','POST','DELETE'])
def marking_as_complete(request,id_in_url):
    if request.method == 'POST':
        changing_status=request.data.get("status")
        if changing_status=="" or changing_status==None:
            return Response(status=400)
        task=Tasks.objects.filter(task_id=id_in_url)
        if len(task)==0:
            return Response(status=404)
        else:
            for t in task:
                if t.status == "completed":
                    return Response(status=400)
            Tasks.objects.filter(task_id=id_in_url).update(status="completed")
            return Response(status=200)
@api_view(['GET'])
def list_of_completed_tasks(request):
    if request.method == 'GET':
        completed_tasks_list=[]
        tasks=Tasks.objects.all()
        for task in tasks:
            if task.status=="completed":
                completed_tasks_list.append({
                    "task_id":task.task_id,
                    "category":task.category,
                    "status":task.status
                })
        return Response(data={
            "List Completed Tasks":completed_tasks_list
        },status=200)
@api_view(['GET'])
def list_of_pending_tasks(request):
    if request.method == 'GET':
        pending_tasks_list=[]
        tasks=Tasks.objects.all()
        for task in tasks:
            if task.status=="pending":
                pending_tasks_list.append({
                    "task_id":task.task_id,
                    "category":task.category,
                    "status":task.status
                })
        return Response(data={
            "List Pending Tasks":pending_tasks_list
        },status=200)