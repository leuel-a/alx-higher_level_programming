#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = malloc(sizeof(listint_t));
	listint_t *list = *head;
	listint_t *prev;

	if (temp == NULL)
		return (NULL);
	temp->n = number;

	if (list == NULL)
	{
		list = &temp;
		temp->next = NULL;
		return (temp);
	}
	while(list)
	{
		if (list->n > temp->n)
		{
			temp->next = list;
			prev->next = temp;
			break;
		}
		prev = list;
		list = list->next;
	}
	return (temp);
}
