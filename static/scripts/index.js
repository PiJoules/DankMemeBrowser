$("#search").submit(function(event){
	event.preventDefault(); // don't refresh page

	var inputs = $(this).serializeArray(); // for some reason, returns an array of objects
	var formObj = {};
	for (var i = 0; i < inputs.length; i++)
		formObj[inputs[i].name] = inputs[i].value;

    if (formObj["q"] !== ""){
        $.get("/", formObj, function(response){
            console.log(response);
            $("#results").empty();
            var tags = response["tags"];
            for (var i in tags){
                $("#results").append("<img src='" + tags[i] + "' />");
            }
        }).fail(function(jqXHR, textStatus, errorThrown){
            alert([textStatus, errorThrown]);
        });
    }
});