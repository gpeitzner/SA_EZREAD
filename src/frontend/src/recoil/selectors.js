import { selector } from "recoil";
import { cartState } from "./atoms";

export const cartStatsState = selector({
  key: 'cartStatsState',
  get: ({ get }) => {
      const cart = get(cartState)
      const totalElements = Object.keys(cart).reduce((acc, value) => {
        const quantity = cart[value].quantity
        if (quantity) {
          return acc + quantity
        }
        return acc
      }, 0)

      return {
        totalElements,
      } 
  }
})