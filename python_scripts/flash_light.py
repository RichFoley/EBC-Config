ATTR_ON_TIME = 'on_time'
ATTR_OFF_TIME = 'off_time'
ATTR_CYCLES = 'cycles'
ATTR_ENTITY_ID = 'entity_id'

on_time = data.get(ATTR_ON_TIME)
off_time = data.get(ATTR_OFF_TIME)
cycles = data.get(ATTR_CYCLES)
entity_id = data.get(ATTR_ENTITY_ID)

logger.debug(f'On time: {on_time}')