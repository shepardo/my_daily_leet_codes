
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn get_decimal_value(head: Option<Box<ListNode>>) -> i32 {
        let mut node = head;
        let mut result = 0;
        while (node != None) {
            //result = result * 2 + *node.val;
            node = node.as_ref().next;
        }
        return result;
    }
}
/*
Line 22, Char 41: no field `val` on type `std::option::Option<std::boxed::Box<list_node::ListNode>>` (solution.rs)
   |
22 |             result = result * 2 + *node.val;
   |                                         ^^^
Line 23, Char 25: no field `next` on type `std::option::Option<std::boxed::Box<list_node::ListNode>>` (solution.rs)
   |
23 |             node = node.next;
   |                         ^^^^
error: aborting due to 2 previous errors
*/

// https://medium.com/swlh/implementing-a-linked-list-in-rust-c25e460c3676
// https://dev.to/felixfaisal/implementing-linked-list-in-rust-3and
// https://users.rust-lang.org/t/populating-a-linked-list-inside-a-loop/26782
// https://aloso.github.io/2021/04/12/linked-list.html
// https://rust-unofficial.github.io/too-many-lists/first-layout.html
// https://discuss.codecademy.com/t/iterate-through-linked-list/504446