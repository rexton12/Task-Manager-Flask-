-- CreateTable
CREATE TABLE "all_jobs" (
    "id" SERIAL NOT NULL,
    "job_name" TEXT NOT NULL,
    "hour" INTEGER NOT NULL,
    "min" INTEGER NOT NULL,
    "sec" INTEGER NOT NULL,

    CONSTRAINT "all_jobs_pkey" PRIMARY KEY ("id")
);
