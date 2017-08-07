import React from 'react'

import TodoItem from './TodoItem'

const TodoList = ({todos, listItem, removeItem, starItem, unstarItem}) => {
	if (!todos) {
		listItem()
		return null
	} else {
		const items = todos.map((todo, index) => <TodoItem item={todo} key={index} removeItem={removeItem} starItem={starItem} unstarItem={unstarItem}/>)
		return <ul>{items}</ul>
	}
}

export default TodoList
