console.log('yo no se ya');
Dropzone.options.monDropzone = {
    init: function() {
        this.on("success", function(file, responseText) {
        // Handle the responseText here. For example, add the text to the preview element:
            console.log(responseText.src);
            console.log('ains');
            $("#app-container").append('<img id=\"generated_img\" src=\"' + responseText.src + '\" alt=\"QR Code\" class=\"resize_qr\">')
        });
    }
};
