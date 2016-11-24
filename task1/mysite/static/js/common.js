function getCookie(name)
{
  var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function galleryCheck()
{
    if (document.getElementById('gallery') !== null)
    {
        if (getCookie('img') === '-1' || getCookie('img') === undefined)
        {
            document.getElementById('gallery_big_img_container').style.display = 'none';
        }
        else
        {
            expandImage(getCookie('img'));
        }
    }
}

function bigImgCheck()
{
    if (getCookie('big_img') !== undefined)
    {
        document.getElementById('background').style.backgroundImage = 'url(' + getCookie('big_img') + ')';
        document.getElementById('background').style.display = "block";

    }
}

function checks()
{
    galleryCheck();
    bigImgCheck();
}

function setCookie(name, value)
{
    document.cookie = name + '=' + value + '; path=/;';
    checks();
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
    checks();
    var help = getHelpElement();
    if (help !== null)
    {
        help.style.display = 'none';
        help.style.whiteSpace = 'pre-wrap';
        help.innerHTML = 'Нажмите F1, чтобы открыть\\закрыть хелп\nНажимайте на миниатюру чтобы увидеть полную картинку\nПеремещение по галерее с помощью стрелок\nESC - закрывает картинку';
    }
}