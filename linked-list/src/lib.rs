//! A linked list implementation in rust

/// A linked list
///
/// Example
/// ```
/// use linked_list::LinkedList;
///
/// let mut list = LinkedList::new();
///
/// list.push(1);
/// list.push(2);
/// list.push(3);
///
/// assert_eq!(list.pop(), Some(3));
/// assert_eq!(list.pop(), Some(2));
/// assert_eq!(list.pop(), Some(1));
/// assert_eq!(list.pop(), None);
/// ```
#[derive(Debug, Clone)]
pub struct LinkedList<T>(Option<Element<T>>);

/// An element of a linked list
#[derive(Debug, Clone)]
struct Element<T> {
    data: T,
    next: Option<Box<Element<T>>>,
}

impl<T> Iterator for LinkedList<T> {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        if let Some(element) = self.0.take() {
            self.0 = element.next.map(|a| *a);
            return Some(element.data);
        };
        return None;
    }
}

impl<T> LinkedList<T> {
    /// Push an element onto the end of the linked list.
    /// O(1) complexity
    ///
    /// # Example
    /// ```
    /// use linked_list::LinkedList;
    ///
    /// let mut list = LinkedList::new();
    ///
    /// list.push(1);
    /// list.push(2);
    /// list.push(3);
    ///
    /// assert_eq!(list.pop(), Some(3));
    /// assert_eq!(list.pop(), Some(2));
    /// assert_eq!(list.pop(), Some(1));
    /// assert_eq!(list.pop(), None);
    /// ```
    pub fn push(&mut self, element: T) {
        if let Some(old) = self.0.take() {
            self.0 = Some(Element {
                data: element,
                next: Some(Box::new(old)),
            })
        } else {
            self.0 = Some(Element {
                data: element,
                next: None,
            })
        }
    }

    /// Pop an element off the end of the linked list
    /// O(1) complexity
    ///
    /// # Example
    ///
    /// ```
    /// use linked_list::LinkedList;
    ///
    /// let mut list = LinkedList::new();
    ///
    /// list.push(1);
    /// list.push(2);
    /// list.push(3);
    ///
    /// assert_eq!(list.pop(), Some(3));
    /// assert_eq!(list.pop(), Some(2));
    /// assert_eq!(list.pop(), Some(1));
    /// assert_eq!(list.pop(), None);
    /// ```
    pub fn pop(&mut self) -> Option<T> {
        return self.0.take().map(|e| {
            self.0 = e.next.map(|e2| *e2);
            e.data
        });
    }

    /// Read an element of the linked list
    /// O(1) complexity
    ///
    /// # Example
    ///
    /// ```
    /// use linked_list::LinkedList;
    ///
    /// let mut list = LinkedList::new();
    ///
    /// list.push(1);
    /// list.push(2);
    /// list.push(3);
    ///
    /// assert_eq!(list.read(), Some(&3));
    /// assert_eq!(list.read(), Some(&3));
    /// ```
    pub fn read(&self) -> Option<&T> {
        return self.0.as_ref().map(|a| &a.data);
    }

    /// Clear the linked list
    ///
    /// # Example
    ///
    /// ```
    /// use linked_list::LinkedList;
    ///
    /// let mut list = LinkedList::new();
    ///
    /// list.push(1);
    /// list.push(2);
    /// list.push(3);
    ///
    /// list.clear();
    ///
    /// assert_eq!(list.pop(), None);
    /// ```
    pub fn clear(&mut self) {
        *self = Self::new();
    }

    /// Create a new linked list
    ///
    /// # Example
    /// 
    /// ```
    /// use linked_list::LinkedList;
    ///
    /// let mut list = LinkedList::<u8>::new();
    ///
    /// assert_eq!(list.pop(), None);
    /// ```
    pub fn new() -> Self {
        return Self(None);
    }
}

impl<T> Default for LinkedList<T> {
    fn default() -> Self {
        Self::new()
    }
}
