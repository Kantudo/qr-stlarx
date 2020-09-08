// document.getElementById("pdf2qr").addEventListener("click", async_app_get("/qr-gen/pdf2qr"));
// document.getElementById("str2qr").onclick = async_app_get("/qr-gen/str2qr");

let default_app = "/qr-gen/pdf2qr";

$("#pdf2qr_tab").click(function() {
    console.log("sr dice pdf2qr");
    async_app_get("/qr-gen/pdf2qr");
});

$("#str2qr_tab").click(function() {
    console.log("sr dice str2qr");
    async_app_get("/qr-gen/str2qr");
});

async_app_get(default_app);

function async_app_get(app) {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : app, // the endpoint
        type : "GET", // http method
        data : { requested_app : app }, // data sent with the post request
        // handle a successful response
        success : function(json) {
            // console.log("success");
            // console.log(json);// another sanity check
            $("#app-container").empty()
            $("#app-container").append(json.app_html)
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
