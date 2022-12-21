from prisma import Prisma
from prisma.models import all_jobs
from flask_apscheduler import APScheduler

prisma=Prisma()
scheduler=APScheduler()

async def create_jobs_resolvers(_,info, input):
    try:
        await scheduler.add_job(trigger='interval', seconds=input['sec'])
        await prisma.connect()
        return await prisma.all_jobs.create(
            data={
                'job_name': input['job_name'],
                'hour': input['hour'],
                'min':input['min'],
                'sec':input['sec']
            }
        )
    finally:
        await prisma.disconnect()
        
        


