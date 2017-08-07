import React from 'react'

const SearchTodo = ({search}) => {
	let searchInput
	const onSubmit = (e) => {
		e.preventDefault()
		search(searchInput.value)
	}
	return <div>
		<form onSubmit={onSubmit}>
			Search:
			<input ref={node => {searchInput = node}}/>
			<button type="submit">
				Search
			</button>
		</form>
	</div>
}

export default SearchTodo
