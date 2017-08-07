import React from 'react'

const TodoItem = ({item, removeItem, starItem, unstarItem}) => {
	const remove = () => removeItem(item.item_id)
	const toggleStar = () => item.starred ? unstarItem(item.item_id) : starItem(item.item_id)
	return <li>
		{item.title}
		<br/>
		{item.content}
		<a onClick={toggleStar}>{item.starred ? '\u2605' : '\u2606'}</a>
		<a onClick={remove}>{'\u2718'}</a>
	</li>
}

export default TodoItem
