export function search(){
    let community_name = []

    console.log("Hello")
    axios.get('https://jsonplaceholder.typicode.com/users')
    .then(function (response) {
    // handle success(axiosの処理が成功した場合に処理させたいことを記述)
        for(let i in response.data) community_name.push(response.data[i].name)
        
        
    })
    .catch(function (error) {
    // handle error(axiosの処理にエラーが発生した場合に処理させたいことを記述)
        console.log(error);
    })
    .finally(function () {
    // always executed(axiosの処理結果によらずいつも実行させたい処理を記述)
        let textbox = " ";
        let url = new URL(window.location.href)
        let params = url.searchParams
        let page;
        let parentDiv = document.getElementById("parent-div");
        params.get('id') == "" ? page = 0 :page = Number(params.get('id'));
        textbox = document.getElementById("search-text");
        while(parentDiv.firstChild) parentDiv.removeChild(parentDiv.firstChild);

        for(let i = page*5;i < (page+1)*5;i++){      
            let linkURL = ""
            if(textbox.value == ""){
                if(community_name[i] == undefined) break;
                var newElement = document.createElement("a"); 
                var newContent = document.createTextNode(`${community_name[i]}`) 
                newElement.appendChild(newContent); 
                // url.searchParams.set('id',i);
                linkURL = `community.html?id=${community_name[i]}`;
                // linkURL = linkURL + community_name[i];
                newElement.href = linkURL
                newElement.classList.add('nav-item')
                newElement.classList.add('nav-link')
                newElement.classList.add('active')
                newElement.classList.add('community')
                newElement.setAttribute("id",`${community_name[i]}`) 
                parentDiv.appendChild(newElement)
            }

            if(textbox.value != ""){
                if(community_name[i] == "") break;
                if(community_name[i].match(textbox.value)) {
                    var newElement = document.createElement("a")
                    var newContent = document.createTextNode(`${community_name[i]}`)
                    newElement.appendChild(newContent)
                    linkURL = linkURL + community_name[i]
                    newElement.href = linkURL
                    newElement.classList.add('nav-item')
                    newElement.classList.add('nav-link')
                    newElement.classList.add('active')
                    newElement.classList.add('community')
                    newElement.setAttribute("id",`${community_name[i]}`)
                    parentDiv.appendChild(newElement)
                }
            } 
        }
    });
   
}

export default search