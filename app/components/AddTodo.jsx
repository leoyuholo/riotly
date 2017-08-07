import React from 'react'

const AddTodo = ({addItem}) => {
	let titleInput, contentInput
	const onSubmit = (e) => {
		e.preventDefault()
		addItem({title: titleInput.value, content: contentInput.value})
	}
	return <div>
		<form onSubmit={onSubmit}>
			Title:
			<input ref={node => {titleInput = node}}/>
			Content:
			<input ref={node => {contentInput = node}}/>
			<button type="submit">
				Add
			</button>
		</form>
	</div>
}

export default AddTodo
