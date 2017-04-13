graph = {};
IMG_DICT = {};
preload_deep = 1;

function ajax(url, func)
{
    var xhr = new XMLHttpRequest();

    xhr.open('GET', url, true);
    xhr.send();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState != 4) return;
        if (xhr.status != 200)
            alert(xhr.status + ': ' + xhr.statusText);
        else
            func(xhr.responseText);
    }
}



function ajax_sync(url, func)
{
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.send();
    return xhr.responseText;
}

function addImageInHash(src)
{
    if (IMG_DICT[src])
       return

    var img = new Image();
    img.onload = function()
    {
        console.log(src + ' Загружено');
        IMG_DICT[src] = 'loaded';
    }
    img.src = src;

    document.getElementById('image-hash').appendChild(img);
}

function setStage(stage)
{
    graph[stage.codename] = stage;
    document.getElementById('img').src = stage.img;
    document.getElementById('text').innerHTML = stage.text;
    setChoices(stage.choices, stage.type);
}

function setChoices(choices, type)
{
    document.getElementById('choices').innerHTML = '';
    document.body.onclick = function() {};
    choices.forEach(function(choice)
    {
        var d = document.createElement('div');
        d.classList.add('choice', 'menu-item');
        d.title = choice.title;
        d.onclick = function() { makeChoice(choice.stage_to)};
        d.innerText = choice.text;
        document.getElementById('choices').appendChild(d);
    });
    choices.forEach(function(choice) { preload_stage(choice.stage_to, 1) });
}

function makeChoice(codeNameNextStage)
{
    function afterResponse(response)
    {
        if (response === 'Читерок')
            return;
        if (graph[codeNameNextStage])
            setStage(graph[codeNameNextStage]);
        else
            setStage(JSON.parse(ajax_sync('getStage/' + codeNameNextStage)));
    }
    ajax('nextStage/' + codeNameNextStage, afterResponse);
}

function preload_stage(codename, deep)
{
    function afterResponse(response)
    {

        stage = JSON.parse(response);
        graph[codename] = stage;
        addImageInHash(stage.img)
    }
    if (deep > 0)
    {
        ajax('getStage/' + codename, afterResponse)
    }
}

window.onload = function (event)
{
    var d = document.createElement('div');
    d.classList.add('no_show');
    d.id = 'image-hash';
    document.body.appendChild(d);
    function afterResponse(response)
    {
        stage = JSON.parse(ajax_sync('getStage/' + response));
        addImageInHash(stage.img);
        setStage(stage);
    }
    ajax('currentStage', afterResponse);
    ajax('vars', function(response) {console.log(response)})
};