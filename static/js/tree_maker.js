document.addEventListener('DOMContentLoaded', () => {

    const mainList = document.querySelector('.js-main-list');

    const getData = () => { // получаем строку с сервера
        return JSON.parse(document.getElementById("json_data").dataset.geocode)
    }

    getData()

    // по клику на кнопку, добавляем класс "active" родителю кнопки
    const listButtonClick = () => {
        let item = event.target;

        item.parentNode.classList.toggle('active');

        if(!item.parentNode.classList.contains('active')){
            item.parentNode.querySelectorAll('.list__item').forEach(item => item.classList.remove('active'));
        }
    }

    // если есть компоненты, то происходит зпись их в дерево
    const addComponents = (item, listItem) => {
        if(item.hasOwnProperty('component')){
            if(item.component.length > 0){
                let compList = document.createElement('ul');
                compList.classList.add('list');

                listItem.classList.add('list__item_has-component');

                let listLi = document.createElement('li');
                listLi.classList.add('list__item');
                item.component.forEach(component => {
                    let listLi = document.createElement('li');
                    listLi.classList.add('list__item');

                    listLi.innerText = component;

                    compList.appendChild(listLi);
                });

                listItem.appendChild(compList);

            }
            else{
                listItem.classList.add('list__item_has-no-component');
            }
        }
    }

    // если есть дети, то мы создаем в элементе списка еще один список, и вызываем ф-цию buildTree, которая возвращает список детей, обернутых в html
    const addChildrens = (item, listItem) => {
        if(item.hasOwnProperty('child')){
            if(item.child.length > 0){
                let innerList = document.createElement('ul');
                innerList.classList.add('list');

                listItem.classList.add('list__item_has-children');
                buildTree(item.child).forEach(item => innerList.appendChild(item));
                listItem.appendChild(innerList);

            }
            // если детей нет - добавляем класс "list__item_has-no-children"
            else{
                listItem.classList.add('list__item_has-no-children');
            }

        }
    }


    const data = getData()

    console.log(data);

    const buildTree = data => {
        let listItems = new Array();

        data.forEach(item => {
            // создаем элемент списка
            let listItem = document.createElement('li');
            listItem.classList.add('list__item');

            // создаем кнопку и вставляем имя папки во внутренний текст
            let listbutton = document.createElement('button');
            listbutton.classList.add('list__button');
            listbutton.innerText = item.name;
            listItem.appendChild(listbutton);
            addComponents(item, listItem);
            addChildrens(item, listItem);
            listItems.push(listItem); // Добавляем элемент в список элементов, который вернет ф-ция
        });

        return listItems;
    }

    if(typeof(data) == 'object'){ // проверяем, что ответ от сервера это объект( массив в js - тоже объект )
        buildTree(data).forEach(item => mainList.appendChild(item)); // mainList - основной список на странице, тут мы добавляем в него всех детей, что возвращает buildTree
    }
    else{
        alert("Error");
    }
    let listItems = document.querySelectorAll('.list__button');

    listItems.forEach(item => item.addEventListener('click', listButtonClick)); // добавляем обработку события клика по кнопке
});
