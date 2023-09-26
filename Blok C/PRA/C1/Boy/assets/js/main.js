function errorBackButton() {
    if (document.referrer == window.location.href) {
        window.location.href = "./index.html";
    }
    else {
        window.history.back();
    };
}