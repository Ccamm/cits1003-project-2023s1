function loadBackground() {
    let symbols = '12345';
    var bgDiv = $(".particle-container");
    for (let sym of symbols) {
        var particleId = "particles-"+sym;
        bgDiv.append(`<div id='${particleId}' class='particles'></div>`);
        particlesJS.load(particleId, `/js/particles/${sym}.json`, () => {});
    }
}

$(document).ready(() => {
    loadBackground();
});