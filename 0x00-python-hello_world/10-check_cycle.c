#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: head of the linked list
 *
 * Return: If cycle is found, it returns 1. Otherwise,
 * it returns 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);

	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
