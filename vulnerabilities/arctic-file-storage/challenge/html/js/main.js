function errorCallback(xhr, status, error) {
    $.notifyBar({
        cssClass: "error", html: `<p>Failed to download file 😭</p>`,
        delay : 3000,
        animationSpeed : "normal"
    });
}

function getResult(data) {
    var id = data.data.id;
    $.notifyBar({
        cssClass: "success",
        html: `<p>Successfully saved file! <a href="/assets/${id}?download">Click here to download</a></p>`,
        delay: 5000,
        animationSpeed: 'normal'
    });
}

function submitURL() {
    var submittedUrl = $("#url").val();

    var body = {
        url: submittedUrl,
        data: {}
    }

    $.ajax({
        url: '/files/import',
        type: 'POST',
        data: JSON.stringify(body),
        contentType: 'application/json',
        dataType: 'json',
        success: getResult,
        error: errorCallback
    });
}

function loadBackground() {
    particlesJS.load('particles-js', '/js/particles.json', function() {});
}

(($) => {
    loadBackground();
    $('#content').delay(500).fadeIn(500);
    $('#submit').on('click', submitURL);
})(jQuery);