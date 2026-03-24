# TLV Parser for EMV Data

This module provides utilities to parse Tag-Length-Value (TLV) encoded data commonly used in EMV specifications.

## Functions

### parse_tlv(tlv_data)

Parses a TLV encoded byte sequence and returns a dictionary representation.

**Parameters:**  
- `tlv_data` (bytes): The TLV encoded data as bytes.

**Returns:**  
- `dict`: A dictionary where each key is the tag, and the value is the corresponding length and value.

### encode_tlv(tag, value)

Encodes a single tag and its value into TLV format.

**Parameters:**  
- `tag` (str): The TLV tag as a hexadecimal string.  
- `value` (bytes): The value to encode for the given tag.

**Returns:**  
- `bytes`: The TLV encoded data as bytes.

## Example Usage

```python
# Example TLV Data
tlv_data = b'9F270180'
parsed = parse_tlv(tlv_data)
print(parsed)
```
