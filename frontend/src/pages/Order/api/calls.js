import { Order } from './index'
import { createClient } from '../../../plugins/axios'

export function createOrder(post) {
    return createClient().post(`${Order}/`, post)
}
export function getPayment(id) {
    return createClient().get(`${Order}/${id}`)
}
export function getUserWisePayment(user_id) {
    return createClient().get(`${Order}/user/${user_id}`)
}

