//コミュニティーの数
// import community_name  from './search.js'
let textbox = " ";
// let community_name = ["勤怠管理システムを作りたい","hello","Machine Learning","S","example","sample"]
// let community_name;
let n = 5

let url = new URL(window.location.href)
let params = url.searchParams
let page = 0;
let user_info
// console.log("hello")


// async function populate() {
//     const requestURL = 'http://52.69.135.133:8888/api/community/';
//     const request = new Request(requestURL);
    
//     const response = await fetch(request);
//     const superHeroesText = await response.text();
//     //console.log(superHeroesText);
    
//     const superHeroes = JSON.parse(superHeroesText);
//     console.log(superHeroes);
//     community_name = superHeroes
// }
//  populate();

// async function populateuser() {
//     const requestURL = 'http://52.69.135.133:8888/api/user/';
//     const request = new Request(requestURL);
//     const response = await fetch(request);
//     const superHeroesText = await response.text();
//     const superHeroes = JSON.parse(superHeroesText);
//     console.log(superHeroes);
//     user_info = superHeroes
// }
//  populateuser();
//  console.log(user_info)
//検索されたときに発火、コミュニティ検索

function search(){
    console.log("Hello")
    let community_name = []
    axios.get('https://jsonplaceholder.typicode.com/users')
    .then(function (response) {
        community_name.length = 0
    // handle success(axiosの処理が成功した場合に処理させたいことを記述)
        for(let i in response.data) community_name.push({"name":response.data[i].name,"id":response.data[i].id})
        
    })
    .catch(function (error) {
    // handle error(axiosの処理にエラーが発生した場合に処理させたいことを記述)
        console.log(error);
    })
    .finally(function () {
        let textbox = " ";
        let url = new URL(window.location.href)
        let params = url.searchParams
        let page;
        let parentDiv = document.getElementById("parent-div");
        params.get('id') == "" ? page = 0 :page = Number(params.get('id'));
        textbox = document.getElementById("search-text");
        while(parentDiv.firstChild) parentDiv.removeChild(parentDiv.firstChild);
        let linkURL =  `${location.protocol}//${location.hostname}/community`;
        for(let i = 0;i < community_name.length;i++){      
            if(textbox.value == ""){
                if(community_name[i]['name'] == undefined) break;
                var newElement = document.createElement("a"); 
                var newContent = document.createTextNode(`${community_name[i]['name']}`) 
                newElement.appendChild(newContent); 
                // url.searchParams.set('id',i);
                // linkURL = linkURL +`?${community_name[i]}`;
                // linkURL ="{% url 'api_app:community' %}"
                // linkURL = linkURL + community_name[i];
                newElement.href = linkURL + `?${community_name[i]['id']}`
                newElement.classList.add('nav-item')
                newElement.classList.add('nav-link')
                newElement.classList.add('active')
                newElement.classList.add('community')
                newElement.setAttribute("id",`${community_name[i]['ud']}`) 
                parentDiv.appendChild(newElement)
            }
            if(textbox.value != ""){
                if(community_name[i]['name'] == "") break;
                if(community_name[i]['name'].match(textbox.value)) {
                    var newElement = document.createElement("a")
                    var newContent = document.createTextNode(`${community_name[i]['name']}`)
                    newElement.appendChild(newContent)
                    // linkURL = linkURL + community_name[i]
                    newElement.href = linkURL + `?${community_name[i]['id']}`
                    newElement.classList.add('nav-item')
                    newElement.classList.add('nav-link')
                    newElement.classList.add('active')
                    newElement.classList.add('community')
                    newElement.setAttribute("id",`${community_name[i]['id']}`)
                    parentDiv.appendChild(newElement)
                }
            } 
        }

    });
 
}   

function NextPage(){
    
    const url = new URL(window.location.href)
    alert(community_name.length)
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
// function show(){
//     // p = document.getElementById('parent-div')
//     console.log(parentDiv)
// }

// search()

// export default { search }


