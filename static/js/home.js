//コミュニティーの数
let textbox = " ";
// let community_name = ["勤怠管理システムを作りたい","hello","Machine Learning","S","example","sample"]
let community_name;
let n = 5
let parentDiv = document.getElementById("parent-div");
let url = new URL(window.location.href)
let params = url.searchParams
let page;
let user_info


async function populate() {
    const requestURL = 'http://52.69.135.133:8888/api/community/';
    const request = new Request(requestURL);
    
    const response = await fetch(request);
    const superHeroesText = await response.text();
    //console.log(superHeroesText);
    
    const superHeroes = JSON.parse(superHeroesText);
    console.log(superHeroes);
    community_name = superHeroes
}
 populate();

async function populateuser() {
    const requestURL = 'http://52.69.135.133:8888/api/user/';
    const request = new Request(requestURL);
    const response = await fetch(request);
    const superHeroesText = await response.text();
    const superHeroes = JSON.parse(superHeroesText);
    console.log(superHeroes);
    user_info = superHeroes
}
 populateuser();
 console.log(user_info)
//検索されたときに発火、コミュニティ検索
function search(){
    
    // URLSearchParamsオブジェクトを取得
    // let start;
    console.log(user_info[0].name)
    console.log(community_name[0])
    params.get('id') == "" ? page = 0 :page = Number(params.get('id'));
    textbox = document.getElementById("search-text");
    while(parentDiv.firstChild) parentDiv.removeChild(parentDiv.firstChild);
    for(let i = page*5;i < (page+1)*5;i++){      
        let linkURL = ""
        if(textbox.value == ""){
            if(community_name[i].name == undefined) break;
            var newElement = document.createElement("a"); 
            var newContent = document.createTextNode(`${community_name[i].name}`) 
            newElement.appendChild(newContent); 
            // url.searchParams.set('id',i);
            linkURL = `community.html?id=${community_name[i].id}`;
            // linkURL = linkURL + community_name[i];
            newElement.href = linkURL
            newElement.classList.add('nav-item')
            newElement.classList.add('nav-link')
            newElement.classList.add('active')
            newElement.classList.add('community')
            newElement.setAttribute("id",`${community_name[i].id}`) 
            parentDiv.appendChild(newElement)
        }
        
        if(textbox.value != ""){
            if(community_name[i].name == "") break;
            if(community_name[i].name.match(textbox.value)) {
                var newElement = document.createElement("a")
                var newContent = document.createTextNode(`${community_name[i].name}`)
                newElement.appendChild(newContent)
                linkURL = linkURL + community_name[i].name
                newElement.href = linkURL
                newElement.classList.add('nav-item')
                newElement.classList.add('nav-link')
                newElement.classList.add('active')
                newElement.classList.add('community')
                newElement.setAttribute("id",`${community_name[i].id}`)
                parentDiv.appendChild(newElement)
            }
        } 
    }
}   

function NextPage(){
    const url = new URL(window.location.href)
    if(community_name.length > page*5)page = page + 1
    url.searchParams.set('id', page);
    location.href = url.href;
}

function PretPage(){
    const url = new URL(window.location.href)
    console.log(url)
    if(page > 0) page = page - 1;
    url.searchParams.set('id', page)
    location.href = url.href
}

function CreatePage(){
    const url = new URL(window.location.href)
    location.href = "file:///C:/Hackathon/View/CreateCommunity.html"
    // console.log(url)
}

