# Dynamic

## Properties

| Name       | Type    | Description                                     |
| ---------- | ------- | ----------------------------------------------- |
| Name       | String  | A string that represents the name of the object |
| Parent     | Dynamic | Returns the parent of the dynamic               |
| Type       | String  | Type of object it is                            |
| BVDID      | String  | Internal Dynamic Node ID                        |
| Replicated | Bool    | Replicates to clients                           |
| Loaded     | Bool    |                                                 |
| Locked     | Bool    |                                                 |

## Functions

| Name                        | Type          | Description                 |
| --------------------------- | ------------- | --------------------------- |
| GetChildren                 | { Dynamic.. } | Returns children in a array |
| Destroy                     | Void          |                             |
| GetDynamicId                | number        |                             |
| SetDynamicId `internalonly` | Void          |                             |
| Destroy                     | Void          | Destroys the object         |
