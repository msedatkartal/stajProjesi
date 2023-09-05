
//image change
function imageChange(input) {
    var imagePreview = document.getElementById('imagePreview');
    var file = input.files[0];
    var reader = new FileReader();

    reader.onload = function (e) {
        imagePreview.src = e.target.result;
    };

    reader.readAsDataURL(file);
}
