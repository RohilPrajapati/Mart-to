import { Dashboard } from './index'
import { createClient } from '../../../plugins/axios'

export function getDashBoardData() {
    return createClient().get(`${Dashboard}/`)
}
