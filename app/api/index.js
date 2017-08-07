
const postOptions = (bodyObj) => {
	return {
		method: 'post',
		headers: new Headers({'Content-Type': 'application/json'}),
		body: JSON.stringify({item_id})
	}
}

const prefix = '/api'

const api = {
	starItem: (item_id) => {
		return fetch(`${prefix}/star`, postOptions({item_id}))
			.then(res => res.json())
			.then(resObj => resObj.result)
	},
	unstarItem: (item_id) => {
		return fetch(`${prefix}/unstar`, postOptions({item_id}))
			.then(res => res.json())
			.then(resObj => resObj.result)
	},
	addItem: ({title, content}) => {
		return fetch(`${prefix}/add`, postOptions({title, content}))
			.then(res => res.json())
			.then(resObj => resObj.result)
	},
	removeItem: (item_id) => {
		return fetch(`${prefix}/remove`, postOptions({item_id}))
			.then(res => res.json())
			.then(resObj => resObj.result)
	},
	listItem: () => {
		return fetch(`${prefix}/list`)
			.then(res => res.json())
			.then(resObj => resObj.result)
	},
	search: (query) => {
		if (!query)
			return api.listItem()
		return fetch(`${prefix}/search/${query}`)
			.then(res => res.json())
			.then(resObj => resObj.result)
	}
}

export default api
