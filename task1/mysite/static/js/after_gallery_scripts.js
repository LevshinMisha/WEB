document.getElementById('gallery').style.display = 'none';
//для начала нужно загрузить гифку, которая показывает что изображение грузится и только потом открывать изображения
load_img = new Image();
load_img.onload = function()
    {
        document.getElementById('gallery_cash').appendChild(load_img);
        document.getElementById('gallery').style.display = 'block';
    };
load_img.src = "/static/files/loading.gif";