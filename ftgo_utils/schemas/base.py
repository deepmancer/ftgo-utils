import pydantic


class BaseModel(pydantic.BaseModel):    
    model_config = pydantic.ConfigDict(from_attributes=True, validate_assignment=True, populate_by_name=True)
