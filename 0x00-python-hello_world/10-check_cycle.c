#include "lists.h"

/**
 * check_cycle - checks if a singly linked list contain a cycle.
 * @list: A singly-linked list
 *
 * Return: If there is no cycle 0 else -1.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
