from IPython import display
from ensure import ensure_annotations
from IPYNBrenderer.custom_exception import InvalidURLException
from IPYNBrenderer.logger import logger
from py_youtube import Data


@ensure_annotations
def get_time_info(URL: str) -> int:
    def  verify_vid_id_len(vid_id, expected_len = 11):
        len_of_vid_id = len(vid_id)
        if len_of_vid_id != expected_len:
            raise InvalidURLException(f"Invalid video id with length : {len_of_vid_id} where as expected is : {expected_len}")
    
    try:
        split_val = 
    

@ensure_annotations
def render_Youtube_video(URL:str, width:int = 780, height:int=160) -> str:
    try:
        if URL is None:
            raise InvalidURLException("URL cannot be none")
        data = Data(URL).data()
        if data["publishdate"] is not None:
            time = get_time_info(URL)
            vid_id = data["id"]
            embed_URL = f"https://www.youtube.com/embed/{vid_id}?start={time}"
            logger.info(f"embed URL: {embed_URL}")
            iframe = f"""<iframe 
            width="{width}" height="{height}" 
            src="{embed_URL}"
            title="YouTube video player"
            frameborder="0" 
            allow="accelerometer; 
            autoplay; 
            clipboard-write; 
            encrypted-media; 
            gyroscope; picture-in-picture"
            allowfullscreen>
            </iframe>
            """
            
            display.display(display.HTML(iframe))
            return "success"
    except Exception as e:
        raise e