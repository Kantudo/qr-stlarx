// Used to safely retrieve csrf token(straight from django wiki)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// AJAX for posting

function asyncimg_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "/qr-gen/str2qr", // the endpoint
        type : "POST", // http method
        data : { str2encode : $('#str2encode').val(),  csrfmiddlewaretoken: getCookie('csrftoken'), }, // data sent with the post request
        // handle a successful response
        success : function(json) {
            $('#str2encode').val(''); // remove the value from the input
            //console.log(json); // log the returned json to the console
            if(document.getElementById("generated_img")){
                $("#generated_img").prop("src", json.src);
            }else{
                $("#app-container").append('<img id=\"generated_img\" src=\"' + json.src + '\" alt=\"QR Code\" class=\"resize_qr\">')
            }
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
$('#str2encode_form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    asyncimg_post();
});
