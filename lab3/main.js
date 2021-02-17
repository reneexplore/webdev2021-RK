let addTodobutton = document.getElementById('addTodo-button');
let toDocontainer = document.getElementById('toDocontainer');
let inputField = document.getElementById('inputField');

addTodobutton.addEventListener('click', function(){
	var paragraph = document.createElement('label');
	paragraph.innerText = inputField.value;
	toDocontainer.appendChild(paragraph);
	inputField.value="";
	paragraph.addEventListener('click', function(){
		paragraph.style.textDecoration = "line-through";
	});
	paragraph.addEventListener('dblclick', function(){
		toDocontainer.removeChild(paragraph);
	});
})