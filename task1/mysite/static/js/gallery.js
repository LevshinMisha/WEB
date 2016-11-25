IMAGE_COUNT = 19;
IMG_DICT = {};
hideHelp();

function pre_download_next_and_prev_image(id)
{
    var int_id = parseInt(id);
    if (int_id !== 0)
        addImageInCash(getImageSrc((int_id - 1).toString()));
    else
        addImageInCash(getImageSrc((IMAGE_COUNT - 1).toString()));
    if (int_id !== IMAGE_COUNT)
        addImageInCash(getImageSrc((int_id + 1).toString()));
    else
        addImageInCash(getImageSrc('0'));
}

function closeBigImage()
{
    setCookie('img', '-1');
}

document.body.onkeydown = function (e)
{
    if (e.keyCode === 112)
    {
        e.preventDefault();
        e.stopImmediatePropagation();
        if (getHelpElement().style.display === 'none')
            showHelp();
        else
            hideHelp();
    }
    if (getCookie('img') !== '-1' && getCookie('img') !== undefined)
    {
        if (e.keyCode === 27)
        {
            closeBigImage();
        }
        if (e.keyCode === 37)
        {
            var c = parseInt(getCookie('img')) - 1
            if (c < 0)
                c = IMAGE_COUNT;
            expandImage(c.toString());
        }
        if (e.keyCode === 39)
        {
            var c = parseInt(getCookie('img')) + 1
            if (c === IMAGE_COUNT + 1)
                c = 0;
            expandImage(c.toString());
        }
    }

}

function getImageSrc(id)
{
    var src_parts = document.getElementById(id).src.split('/');
    var src = '';
    for (var i = 0; i < src_parts.length; i++)
    {
        if (src_parts[i] !== 'thumbnails')
            {
                if (i !== src_parts.length - 1)
                    src += src_parts[i] + '/';
                else
                    src += src_parts[i].slice(0, -7) + '.jpg';
            }

    }
    return src;
}

function expandImage(id)
{
    document.cookie = 'img=' + id + '; path=/;';
    document.getElementById("gallery_big_img").style.opacity = 0.5;
    var src = getImageSrc(id);
    pre_download_next_and_prev_image(id);
    document.getElementById('gallery_big_img').style.display = 'none';
    document.getElementById('gallery_big_img').src = src;
    document.getElementById('gallery_big_img').style.display = 'inline-block';
    document.getElementById('gallery_big_img_container').style.display = 'flex';
    document.getElementById('button_make_img_background').onclick = makeBackgroundImage(src);

}

function imgOnClick(id)
{
    setCookie('img', id.toString());
}

function bigImgOnLoad(id)
{
    document.getElementById("gallery_big_img").style.opacity = 1;
}

function makeBackgroundImage(url)
{
    return function (event)
    {
        setCookie('big_img', url);
    }
}

function addImageInCash(url)
{
    if (!IMG_DICT[url])
    {
        IMG_DICT[url] = true;
        var image = new Image();
        image.src = url;
        console.log(url + ' Загружается');
        image.onload = function()
        {
            console.log(url + ' Загружено');
        }
        document.getElementById('gallery_cash').appendChild(image);
    }

}