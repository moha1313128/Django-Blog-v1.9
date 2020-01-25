==============================================================
	name 		Method		Authentication		Description                            
==============================================================
	CREATE		POST		yes					Make new
	RETRIEVE	GET			no					List / Search
	UPDATE		PUT/PATCH	yes					Edit	
	DELETE		DELETE		yes					Delete 


index <a href='{% url "detail" id=obj.id %}'>{{ obj.title}}</a></br> 
