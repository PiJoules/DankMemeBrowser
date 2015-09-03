// $("#search").submit(function(event){
// 	event.preventDefault(); // don't refresh page

// 	// var inputs = $(this).serializeArray(); // for some reason, returns an array of objects
// 	// var formObj = {};
// 	// for (var i = 0; i < inputs.length; i++)
// 	// 	formObj[inputs[i].name] = inputs[i].value;
//  //    /**
//  //     * Will include channel, description, time, and captcha
//  //     */

// 	// if (formObj["g-recaptcha-response"] === ""){
// 	// 	alert("Please prove you are human.");
// 	// 	return;
// 	// }

//     //if (content !== "" && formObj["channel"] !== ""){
//         $.get("/", formObj, function(response){
//             console.log(response);
//             // if (response !== ""){
//             //     alert(response);
//             //     location.reload();
//             // }
//             // else {
//             //     // success
//             //     window.location.href = "/" + formObj.channel;
//             // }
//         }).fail(function(jqXHR, textStatus, errorThrown){
//             alert([textStatus, errorThrown]);
//         });
//     //}
// });