==============================================================
	name 		Method		Authentication		Description                            
==============================================================
	CREATE		POST		yes					Make new
	RETRIEVE	GET			no					List / Search
	UPDATE		PUT/PATCH	yes					Edit	
	DELETE		DELETE		yes					Delete 


index <a href='{% url "detail" id=obj.id %}'>{{ obj.title}}</a></br> 


model	# return "/posts/%s/"  %(self.id)	

 if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                Post.objects.filter(id = id).update(title= request.POST.get('title'), content= request.POST.get('content'))

                messages.success(request, "Your post has been successfully updated")

                context={'eachpost': eachpost}


                return HttpResponseRedirect("/posts/{id}/".format(id= eachpost.id))  

        else:
            context={'eachpost': eachpost}
            return render(request,'posts/edit.html', context)
