#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	while (list)
	{
		slow = list->next;
		fast = list->next->next;
		if (slow == fast)
			return (1);
		list = list->next;
	}
	return (0);
}
