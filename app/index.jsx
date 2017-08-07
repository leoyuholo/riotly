import {render} from 'react-dom'
import {createStore} from 'redux'
import React from 'react'

import App from './containers/App'
import rootReducer from './reducers'

const store = createStore(
	rootReducer,
	{},
	window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
)

render(
	<App store={store}/>,
	document.getElementById('root')
)
