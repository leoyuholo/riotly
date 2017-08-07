import {connect} from 'react-redux'
import React from 'react'

import TodoList from '../components/TodoList'
import AddTodo from '../components/AddTodo'
import SearchTodo from '../components/SearchTodo'
import api from '../api'
import * as actions from '../actions'
import * as types from '../actions/types'

const App = ({items, listItem, addItem, removeItem, starItem, unstarItem, search}) => {
	return <div>
		<SearchTodo search={search}/>
		<TodoList todos={items} listItem={listItem} removeItem={removeItem} starItem={starItem} unstarItem={unstarItem}/>
		<AddTodo addItem={addItem}/>
	</div>
}

const mapStateToProps = (state) => {
	return {
		items: state.items
	}
}

const mapDispatchToProps = (dispatch) => {
	return {
		starItem: (item_id) => {
			return api.starItem(item_id)
				.then(item => dispatch(actions.updateItem(item)))
		},
		unstarItem: (item_id) => {
			return api.unstarItem(item_id)
				.then(item => dispatch(actions.updateItem(item)))
		},
		addItem: ({title, content}) => {
			return api.addItem({title, content})
				.then(item => dispatch(actions.addItem(item)))
		},
		removeItem: (item_id) => {
			return api.removeItem(item_id)
				.then(result => result ? dispatch(actions.removeItem(item_id)) : console.error(`Remove failed for item ${item_id}`))
		},
		listItem: () => {
			return api.listItem()
				.then(items => dispatch(actions.listItem(items)))
		},
		search: (query) => {
			return api.search(query)
				.then(items => dispatch(actions.listItem(items)))
		}
	}
}

export default connect(mapStateToProps, mapDispatchToProps)(App)
