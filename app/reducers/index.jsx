import {combineReducers} from 'redux'
import _ from 'lodash'

import * as types from '../actions/types'

const items = (state = false, action) => {
	switch (action.type) {
		case types.LIST_ITEM:
			return action.items
		case types.ADD_ITEM:
			return state.concat([action.item])
		case types.UPDATE_ITEM:
			return state.map(item => item.item_id === action.item.item_id ? action.item : item)
		case types.REMOVE_ITEM:
			return state.filter(item => item.item_id !== action.item_id)
		default:
			return state
	}
}
export default combineReducers({
	items
})
