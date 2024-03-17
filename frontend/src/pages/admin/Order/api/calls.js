import { Order } from './index'
import { createClient } from '../../../../plugins/axios'

export function getAllPayment(params = {}) {
    return createClient().get(`${Order}/`,{params})
}
export function getPayment(id) {
    return createClient().get(`${Order}/${id}/`)
}
export function updatePayment(id) {
    return createClient().put(`${Order}/${id}/`)
}
