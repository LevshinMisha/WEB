IMAGE_COUNT = 19;
IMG_DICT = {};
CURRENT_COMMENTS = [];
CURRENT_LIKES = '';
CURRENT_ID = '';

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
    CURRENT_ID = '-1';
    document.location = '#-1';
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
    CURRENT_COMMENTS = [];
    CURRENT_LIKES = '';
    if (CURRENT_ID !== id && CURRENT_ID !== -1)
    {
        clearComments();
        CURRENT_ID = id;
        document.location = '#' + id;
        document.getElementById('comments').innerHTML = '<div class="comment" style="padding: 5px">Loading...</div>';
        document.getElementById('like_button').innerText= "Лайки не загрузились";
        document.cookie = 'img=' + id + '; path=/;';
        document.getElementById("gallery_big_img").style.opacity = 0.7;
        var src = getImageSrc(id);

        addImageInCash(src);
        pre_download_next_and_prev_image(id);

        if (document.getElementById('gallery_big_img_container').style.display !== 'flex')
            document.getElementById('gallery_big_img_container').style.display = 'flex';

        document.getElementById('button_make_img_background').onclick = makeBackgroundImage(src);
        if (IMG_DICT[src] !== 'loaded') // Этот костыль я посвещаю работе атрибута src в firefox.
        {
            document.getElementById('gallery_big_img').src = "";
            window.setTimeout(function()
            {
                document.getElementById('gallery_big_img').src = src;
            }, 50)
        }
        else
            document.getElementById('gallery_big_img').src = src;
        window.setTimeout(function()
            {
                getComments();
                getLikes();
            }, 500)
    }
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

function addImageInCash(src)
{
    if (!IMG_DICT[src])
    {
        IMG_DICT[src] = 'loading';
        var image = new Image();
        image.src = src;
        console.log(src + ' Загружается');
        image.onload = function()
        {
            console.log(src + ' Загружено');
            IMG_DICT[src] = 'loaded';
        }
        document.getElementById('gallery_cash').appendChild(image);
    }

}

function ajax(url, func)
{
    var xhr = new XMLHttpRequest();

    xhr.open('GET', url, true);
    xhr.send();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState != 4) return;
        if (xhr.status != 200)
        {
            alert(xhr.status + ': ' + xhr.statusText);
        }
        else
        {
            func(xhr.responseText);
        }
    }
}

function isCommentsNeedToUpdate(comments)
{
    if (comments.length !== CURRENT_COMMENTS.length)
        return true
    for(var i = 0; i < comments.length; i++)
    {
        if (comments[i].author !== CURRENT_COMMENTS[i].author || comments[i].text !== CURRENT_COMMENTS[i].text)
            return true
    }
    return false
}

function clearComments()
{
    document.getElementById('comments').innerHTML = '';
}

function getComments()
{
    function afterResponse(responseText)
    {
        var comments = JSON.parse(responseText);
        if (isCommentsNeedToUpdate(comments.comments))
        {
            CURRENT_COMMENTS = comments.comments;
            clearComments()
            for (var i = 0; i < comments.comments.length; i++)
            {
                var text = comments.comments[i].text;
                var comment = createElement('div', 'comment', '');
                comment.appendChild(createElement('div', 'comment_author', comments.comments[i].author));
                comment.appendChild(createElement('div', 'comment_text', comments.comments[i].text));
                document.getElementById('comments').appendChild(comment)
            }
        }
        else
        {
            if (CURRENT_COMMENTS.length === 0)
                clearComments();
        }

    }

    var picture = getCookie('img');
    if (picture !== '-1')
        ajax('getComments/' + picture, afterResponse)
}

function addComment()
{
    function afterResponse(responseText)
    {
        alert(responseText);
        getComments();
    }

    var picture = getCookie('img');
    var text = document.getElementById('new_comment_text').value;
    text = 'addComment/' + picture + '/' + text;
    var ajaxText = '';
    for (var i in text.split('\n'))
        ajaxText += text.split('\n')[i] + '\\n';
    ajax(ajaxText.slice(0, ajaxText.length - 2), afterResponse)
}

function like()
{
    function afterResponse(responseText)
    {
        getLikes()
    }

    var picture = getCookie('img');
    ajax('like/' + picture, afterResponse)
}

function getLikes()
{
    function afterResponse(responseText)
    {
        if (responseText !== CURRENT_LIKES)
        {
            CURRENT_LIKES = responseText;
            document.getElementById('like_button').innerText= "Лайков:" + responseText;
        }
    }

    var picture = getCookie('img');
    if (picture !== '-1')
        ajax('getLikes/' + picture, afterResponse)
}

function downloadXls()
{
    window.location = 'xls';
}

function checkLocation()
{
    if (document.location.hash === '#-1')
    {
        if (CURRENT_ID !== '-1')
            closeBigImage()
    }
    else if (document.location.hash !== '')
        expandImage(document.location.hash.slice(1, document.location.length))
}