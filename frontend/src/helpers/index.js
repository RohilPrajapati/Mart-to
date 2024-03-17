
import { Store } from '../store/index.js'
export function getAuthHeader () {
  const accesstoken = Store.state.user.auth.access

  if (accesstoken) {
    return { Authorization: 'Bearer ' + accesstoken }
  } else {
    return {}
  }
}

export function logout () {
  const data = {}
  Store.dispatch('user/storetoken', data)
  Store.dispatch('user/storeuser', data)
}
