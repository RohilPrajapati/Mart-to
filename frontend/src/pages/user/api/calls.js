import { User } from './index'
// import httpClient from '../../../plugins/axios'
import { createClient } from '../../../plugins/axios'

export function getUserData (params = {}) {
  return createClient().get(`${User}`, { params })
}
export function createUser (post) {
  return createClient().post(`${User}/registration/`,  post )
}
export function loginUser (post) {
    return createClient().post(`${User}/login/`,  post )
}
export function getProfile (user_id) {
  return createClient().get(`${User}/${user_id}/`)
}