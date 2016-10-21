IMAGE_COUNT = 19;

function getCookie(name)
{
  var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}


function getHelpElement()
{
    return document.getElementById('help')
}


function showHelp()
{
    getHelpElement().style.display = 'block';
}

function hideHelp()
{
    getHelpElement().style.display = 'none';
}

window.onload = function (event)
{
    getHelpElement().style.display = 'none';
    getHelpElement().style.whiteSpace = 'pre-wrap';
    getHelpElement().innerHTML = 'Нажмите F1, чтобы открыть\\закрыть хелп\nНажимайте на миниатюру чтобы увидеть полную картинку\nПеремещение по галерее с помощью стрелок\nESC - закрывает картинку';
    cookieChange();
}

function closeBigImage()
{
    document.cookie = 'img=-1';
    cookieChange();
}

document.body.onkeydown = function (e)
{
    console.log(e.keyCode);
    if (e.keyCode === 112)
        if (getHelpElement().style.display === 'none')
            showHelp();
        else
            hideHelp();
    if (e.keyCode === 27)
    {
        closeBigImage();
    }
    if (e.keyCode === 37)
    {
        var c = parseInt(getCookie('img')) - 1
        if (c === -1)
            c = IMAGE_COUNT;
        document.cookie = 'img=' + c.toString();
        cookieChange();
    }
    if (e.keyCode === 39)
    {
        var c = parseInt(getCookie('img')) + 1
        if (c === IMAGE_COUNT + 1)
            c = 0;
        document.cookie = 'img=' + c.toString();
        cookieChange();
    }
}

function expandImage(id)
{
    document.cookie = 'img=' + id;
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
    document.getElementById('gallery_big_img').src = src;
}

function cookieChange()
{
    console.log(getCookie('img'));
    console.log(document.cookie);
    if (getCookie('img') === '-1' || getCookie('img') === undefined)
    {
        document.getElementById('gallery').style.display = 'block';
        document.getElementById('gallery_big_img_container').style.display = 'none';
    }
    else
    {
        document.getElementById('gallery').style.display = 'none';
        expandImage(getCookie('img'));
        document.getElementById('gallery_big_img_container').style.display = 'block';
    }
}

function imgOnClick(id)
{
    document.cookie = 'img=' + id;
    cookieChange();
}

