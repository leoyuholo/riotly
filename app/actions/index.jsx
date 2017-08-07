import * as types from './types'

export const addItem = (item) => {
	return {
		type: types.ADD_ITEM,
		item
	}
}

export const listItem = (items) => {
	return {
		type: types.LIST_ITEM,
		items
	}
}

export const updateItem = (item) => {
	return {
		type: types.UPDATE_ITEM,
		item
	}
}

export const removeItem = (item_id) => {
	return {
		type: types.REMOVE_ITEM,
		item_id
	}
}
